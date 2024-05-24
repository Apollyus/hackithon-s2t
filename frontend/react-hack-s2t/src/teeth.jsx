import React from 'react';
import { Link } from 'react-router-dom';

const Welcome = () => {
  return (
    <div>
      <h1 className='text-slate-700'></h1>
      <Link to="/app">Go to App</Link>
    </div>
  );
};

export default Welcome;