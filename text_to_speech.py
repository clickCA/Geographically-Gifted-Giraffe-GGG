from google.cloud import texttospeech

TEXT = "Hello, World!"


def text_to_speech(text):
    output_file = "speech_" + str(hash(text[:5])) + ".mp3"
    try:
        client = texttospeech.TextToSpeechClient()
        synthesis_input = texttospeech.SynthesisInput(text=text)
        voice = texttospeech.VoiceSelectionParams(
            language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
        )
        audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.MP3
        )
        response = client.synthesize_speech(
            input=synthesis_input, voice=voice, audio_config=audio_config
        )
        with open(output_file, "wb") as out:
            # Write the response to the output file.
            out.write(response.audio_content)
            print("Audio content written to file", output_file)
    except Exception as e:
        print("Cannot convert text to speech")
        print(e)
    return output_file


def main():
    # The response's audio_content is binary.
    file_path = text_to_speech(TEXT)
    print(file_path)

if __name__ == "__main__":
    main()
