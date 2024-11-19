import os
from gtts import gTTS
from moviepy.editor import TextClip, AudioFileClip, CompositeVideoClip

def generate_sentence_by_sentence_video(text, output_filename="output_sentence_by_sentence.mp4"):
    """
    Generate a video with text appearing sentence by sentence and synchronized with audio narration.
    Args:
        text (str): The input text.
        output_filename (str): The output video file.
    """
    # Split text into sentences
    sentences = text.split(". ")
    sentences = [sentence.strip() + ("." if not sentence.endswith(".") else "") for sentence in sentences]

    # Generate audio from the entire text
    tts = gTTS(text)
    audio_file = "audio.mp3"
    tts.save(audio_file)

    # Load the generated audio
    audio = AudioFileClip(audio_file)
    audio_duration = audio.duration

    # Calculate the duration for each sentence
    sentence_duration = audio_duration / len(sentences)

    # Create a list of TextClip objects, one for each sentence
    clips = []
    current_time = 0.0

    for sentence in sentences:
        # Create a TextClip for the sentence
        text_clip = TextClip(sentence, fontsize=50, color='white', size=(1280, 720), bg_color='black', method="caption")
        text_clip = text_clip.set_start(current_time).set_duration(sentence_duration)
        clips.append(text_clip)
        current_time += sentence_duration

    # Combine all TextClips into a single video
    video = CompositeVideoClip(clips, size=(1280, 720))

    # Add the audio to the video
    video = video.set_audio(audio)

    # Write the final video to file
    video.write_videofile(output_filename, fps=24)

    # Cleanup
    os.remove(audio_file)

# Example usage
story_text = (
    "This is the first sentence of the story. Here comes the second sentence. "
    "The third sentence provides more context. Finally, we conclude with the last sentence."
)
generate_sentence_by_sentence_video(story_text, "sentence_by_sentence_video.mp4")