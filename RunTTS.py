from tts.call_synthesize import call_synthesize
from argparse import ArgumentParser
from address_provider import AddressProvider
from pathlib import Path
from tts.audio_player import AudioPlayer
from scipy.io import wavfile
import pyttsx3 as tts


def tts_args(address: str, output_path: [Path or str] = "TechmoTTS.wav"):
    parser = ArgumentParser()
    parser.add_argument("-s", "--service-address", dest="service", default=address,
                        help="An IP address and port (address:port) of a service the client connects to.",
                        type=str)
    parser.add_argument("--session-id", dest="session_id", default="",
                        help="A session ID to be passed to the service. If not specified, the service generates a default session ID.",
                        type=str)
    parser.add_argument("--grpc-timeout", dest="grpc_timeout", default=0,
                        help="A timeout in milliseconds used to set gRPC deadline - how long the client is willing to wait for a reply from the server (optional).",
                        type=int)
    parser.add_argument("--list-voices", dest="list_voices", action='store_true', default=False,
                        help="Lists all available voices.")
    parser.add_argument("-r", "--response", dest="response", default="streaming",
                        help="streaming or single, calls the streaming (default) or non-streaming version of Synthesize.",
                        type=str)
    parser.add_argument("-t", "--text", dest="text", default="Hej",  # input_text,
                        help="A text to be synthesized.", type=str)
    parser.add_argument("-i", "--input-text-file", dest="inputfile", default="",
                        help="A file with text to be synthesized.", type=str)
    parser.add_argument("-o", "--out-path", dest="out_path", default=output_path,
                        help="A path to the output wave file with synthesized audio content.", type=str)
    parser.add_argument("-f", "--sample-rate", dest="sample_rate", default=0,
                        help="A sample rate in Hz of synthesized audio. Set to 0 (default) to use voice's original sample rate.",
                        type=int)
    parser.add_argument("--ae", "--audio-encoding", dest="audio_encoding", default="pcm16",
                        help="An encoding of the output audio, pcm16 (default) or ogg-vorbis.", type=str)
    parser.add_argument("--sp", "--speech-pitch", dest="speech_pitch", default=1.0,
                        help="Allows adjusting the default pitch of the synthesized speech (optional, can be overriden by SSML).",
                        type=float)
    parser.add_argument("--sr", "--speech-range", dest="speech_range", default=1.0,
                        help="Allows adjusting the default range of the synthesized speech (optional, can be overriden by SSML).",
                        type=float)
    parser.add_argument("--ss", "--speech-rate", dest="speech_rate", default=1.0,
                        help="Allows adjusting the default rate (speed) of the synthesized speech (optional, can be overriden by SSML).",
                        type=float)
    parser.add_argument("--sv", "--speech-volume", dest="speech_volume", default=1.0,
                        help="Allows adjusting the default volume of the synthesized speech (optional, can be overriden by SSML).",
                        type=float)
    parser.add_argument("--vn", "--voice-name", dest="voice_name", default="",
                        help="A name od the voice used to synthesize the phrase (optional, can be overriden by SSML).",
                        type=str)
    parser.add_argument("--vg", "--voice-gender", dest="voice_gender", default="",
                        help="A gender of the voice - female or male (optional, can be overriden by SSML).",
                        type=str)
    parser.add_argument("--va", "--voice-age", dest="voice_age", default="",
                        help="An age of the voice - adult, child, or senile (optional, can be overriden by SSML).",
                        type=str)
    parser.add_argument("-l", "--language", dest="language", default="",
                        help="ISO 639-1 language code of the phrase to synthesize (optional, can be overriden by SSML).",
                        type=str)
    parser.add_argument("--play", dest="play", default=False, action="store_true",
                        help="Play synthesized audio. Works only with pcm16 (default) encoding.")
    parser.add_argument("--tls-dir", dest="tls_directory", default="",
                        help="If set to a path with SSL/TLS credential files (client.crt, client.key, ca.crt), use SSL/TLS authentication. Otherwise use insecure channel (default).",
                        type=str)

    # Parse and validate options
    args = parser.parse_args()
    return args

def text2speech(output_path:[Path or str] ="TTS_PL.wav", input_text:str = "Brak tekstu"):
    ap = AddressProvider()
    address = ap.get("tts-pl")
    tts_args_pl = tts_args(address, output_path=output_path)
    call_synthesize(tts_args_pl, input_text)

def talk2us(output_path:[Path or str] ="TTS_PL.wav"):
    sampling_rate, data = wavfile.read(output_path)
    glosnik = AudioPlayer(sample_rate_hertz=sampling_rate)
    glosnik.start(sampling_rate)
    glosnik.append(data)
    glosnik.stop()

def no_techmo_tts(input_text:str = "Brak tekstu"):
    newTTS = tts.init()
    newTTS.setProperty('rate', 120)
    newTTS.say(input_text)
    newTTS.runAndWait()

