import React, { useState } from 'react';

function App() {
  const [selectedFile, setSelectedFile] = useState(null);
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);
  const [isLoading, setIsLoading] = useState(false);

  const fileSelectedHandler = event => {
    const file = event.target.files[0];
    const validMimeTypes = ['audio/mpeg', 'audio/mp4'];

    if (validMimeTypes.includes(file.type)) {
      setSelectedFile(file);
      setError(null); // clear any previous error
    } else {
      setError('Invalid file type. Please select an MP3, MP4, MPEG, M4A file.');
      event.target.value = null; // deselect the file
    }
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
    // Your existing fetchTranscription code here...
  };

  return (
    <div>
      <input type="file" accept="audio/mpeg, audio/mp4" onChange={fileSelectedHandler} />
      <button onClick={fileUploadHandler}>Upload</button>
      {isLoading && <p>Loading...</p>}
      {error && <p>{error}</p>}
      {data && <p>{data.text}</p>}
    </div>
  );
}
export default App;