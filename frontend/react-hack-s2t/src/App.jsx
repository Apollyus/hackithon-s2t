import React, { useState, useEffect } from 'react';

function App() {
  const [data, setData] = useState(null);
  const [selectedFile, setSelectedFile] = useState();

  const fileSelectedHandler = event => {
    setSelectedFile(event.target.files[0]);
  };

  const fileUploadHandler = () => {
    const formData = new FormData();
    formData.append('file', selectedFile); // appending file
    fetch('http://127.0.0.1:8000/upload', {
      method: 'POST',
      body: formData,
    })
    .then(response => response.json())
    .then(data => setData(data));
  };

  useEffect(() => {
    fetch('http://127.0.0.1:8000/') // replace with the URL of your Python app
      .then(response => response.json())
      .then(data => setData(data));
  }, []);

  return (
    <div>
      <input type="file" onChange={fileSelectedHandler} />
      <button onClick={fileUploadHandler}>Upload</button>
      {data && <pre>{data.text}</pre>}
    </div>
  );
}

export default App;