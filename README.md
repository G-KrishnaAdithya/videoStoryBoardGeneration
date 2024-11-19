
# Video Storyboard Generation

This project generates a video with text appearing sentence by sentence, synchronized with audio narration. It utilizes the `gTTS` library for text-to-speech conversion and `moviepy` for video editing.

## Features

- Converts input text into a video.
- Narrates the text using generated audio.
- Displays sentences one by one in synchronization with the narration.

## Prerequisites

Make sure you have Python installed. 
Also make sure that you have required dependencies installed To know the required dependencies used refer to Dependencies_Installation_Guide.md for installing the dependencies
It's recommended to use a virtual environment for this project.

## Installation

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Place your input text in the script or modify the `story_text` variable directly.

2. Run the script:
   ```bash
   python videoGen.py
   ```

3. The generated video will be saved as `sentence_by_sentence_video.mp4` in the current directory.

## Requirements

This project requires the following Python libraries:
- `gtts` for text-to-speech conversion.
- `moviepy` for video creation and editing.

You can find these dependencies listed in the `requirements.txt` file.

## Example

Here's an example of the input text used in the script:

```python
story_text = (
    "This is the first sentence of the story. Here comes the second sentence. "
    "The third sentence provides more context. Finally, we conclude with the last sentence."
)
```

The output will be a video displaying the sentences one by one, synchronized with the audio narration.

## Cleanup

The script automatically removes intermediate audio files after creating the video.

## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute.

## Acknowledgments

- [gTTS](https://github.com/pndurette/gTTS)
- [MoviePy](https://zulko.github.io/moviepy/)
