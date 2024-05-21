import React, { useState, useRef } from 'react';

function App() {
  const [selectedFile, setSelectedFile] = useState(null);
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [transcriptionSuccess, setTranscriptionSuccess] = useState(false);
  const [recording, setRecording] = useState(false);
  const [audioURL, setAudioURL] = useState('');
  const mediaRecorder = useRef(null);

  const startRecording = () => {
    navigator.mediaDevices.getUserMedia({ audio: true })
      .then(stream => {
        mediaRecorder.current = new MediaRecorder(stream);
        mediaRecorder.current.start();

        const audioChunks = [];
        mediaRecorder.current.addEventListener('dataavailable', event => {
          audioChunks.push(event.data);
        });

        mediaRecorder.current.addEventListener('stop', () => {
          const audioBlob = new Blob(audioChunks);
          const audioUrl = URL.createObjectURL(audioBlob);
          const audio = new Audio(audioUrl);
          setSelectedFile(audioBlob); // set selectedFile with the recorded audio
          setAudioURL(audioUrl);
        });

        setRecording(true);
      });
  };

  const stopRecording = () => {
    if (mediaRecorder.current) {
      mediaRecorder.current.stop();
      setRecording(false);
    }
  };

  const fileSelectedHandler = event => {
    setSelectedFile(event.target.files[0]);
  };

  const fileUploadHandler = () => {
    if (!selectedFile) {
      setError('No file selected. Please select a valid file.');
      return;
    }

    setIsLoading(true); // start loading
    const formData = new FormData();
    formData.append('file', selectedFile); // appending file
    fetch('http://127.0.0.1:8000/upload', {
      method: 'POST',
      body: formData,
    })
    .then(response => response.json())
    .then(data => {
      // Call the transcription endpoint after the file has been uploaded
      fetchTranscription(data.filename);
    })
    .finally(() => setIsLoading(false)); // end loading
  };

  const fetchTranscription = (filename) => {
    fetch(`http://127.0.0.1:8000/transcribe/${filename}`)
      .then(response => response.json())
      .then(data => {
        setData(data);
        setTranscriptionSuccess(true); // set transcriptionSuccess to true here
      })
      .catch(() => {
        setError('Transcription failed. Please try again.');
        setTranscriptionSuccess(false);
      });
    // ... rest of your code
  };

  return (
    <div>
      <button onClick={recording ? stopRecording : startRecording}>
        {recording ? 'Stop Recording' : 'Start Recording'}
      </button>
      {audioURL && <audio src={audioURL} controls />}
      <input type="file" accept="audio/mpeg, audio/mp4" onChange={fileSelectedHandler} />
      <button onClick={fileUploadHandler}>Upload</button>
      {isLoading && <p>Loading...</p>}
      {error && <p className="text-red-500 bg-red-100 p-2 rounded">{error}</p>}
      {transcriptionSuccess && <p className="text-green-500 bg-green-100 p-2 rounded">Transcription was successful!</p>}
      {data && <p>{data.text}</p>}
    </div>
  );
}

export default App;