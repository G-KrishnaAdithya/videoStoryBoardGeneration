import os
from gtts import gTTS
from moviepy.editor import TextClip, AudioFileClip, CompositeVideoClip, concatenate_audioclips

def generate_sentence_by_sentence_video(text, output_filename="output_sentence_by_sentence.mp4"):
    """
    Generate a video with text appearing sentence by sentence and synchronized with audio narration.
    Args:
        text (str): The input text.
        output_filename (str): The output video file.
    """
    # Split text into sentences and filter out empty strings
    sentences = text.split(". ")
    sentences = [sentence.strip() + ("." if not sentence.endswith(".") else "") for sentence in sentences if sentence.strip()]

    # Initialize lists for audio files and durations
    audio_files = []
    sentence_durations = []
    valid_sentences = []

    for i, sentence in enumerate(sentences):
        try:
            # Generate audio for each valid sentence
            tts = gTTS(sentence)
            audio_file = f"audio_{i}.mp3"
            tts.save(audio_file)
            audio_files.append(audio_file)

            # Get the duration of the audio
            audio_clip = AudioFileClip(audio_file)
            sentence_durations.append(audio_clip.duration)
            valid_sentences.append(sentence)  # Only include valid sentences
            audio_clip.close()
        except Exception as e:
            print(f"Skipping sentence {i}: '{sentence}' due to error - {e}")

    # If no valid audio generated, exit gracefully
    if not audio_files:
        print("No valid sentences to process. Exiting.")
        return

    # Calculate the start times for each sentence
    start_times = [0] + [sum(sentence_durations[:i + 1]) for i in range(len(sentence_durations) - 1)]

    # Create a list of TextClip objects, one for each valid sentence
    clips = []

    for i, sentence in enumerate(valid_sentences):
        # Create a TextClip for the sentence
        text_clip = TextClip(sentence, fontsize=20, color='white', size=(1280,720), bg_color='black', method="caption")
        text_clip = text_clip.set_position(("center", "bottom"))
        text_clip = text_clip.set_start(start_times[i]).set_duration(sentence_durations[i])
        clips.append(text_clip)

    # Combine all TextClips into a single video
    video = CompositeVideoClip(clips, size=(1280, 720))

    # Combine all audio files into a single AudioFileClip
    audio_clips = [AudioFileClip(audio_file) for audio_file in audio_files]
    combined_audio = concatenate_audioclips(audio_clips)

    # Add the combined audio to the video
    video = video.set_audio(combined_audio)

    # Write the final video to file
    video.write_videofile(output_filename, fps=24)

    # Cleanup
    for audio_file in audio_files:
        os.remove(audio_file)

# Example usage
print("Enter your story below (sentences separated by periods):")
user_story = input()

# Generate video from the user's input
generate_sentence_by_sentence_video(user_story, "user_storyboard_video.mp4")
