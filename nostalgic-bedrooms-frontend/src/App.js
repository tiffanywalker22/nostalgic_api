import React from 'react';
import BedroomList from './components/BedroomList';
import './App.css';

const App = () => {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Nostalgic Bedrooms</h1>
      </header>
      <main>
        <BedroomList />
      </main>
    </div>
  );
};

export default App;
