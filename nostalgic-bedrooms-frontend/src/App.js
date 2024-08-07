import React from 'react';
import BedroomList from './components/BedroomList';
import './App.css';
import { MouseTrail } from 'retro-react';

const App = () => {
  return (
    <div className="App">
      <MouseTrail
        offset={{
          x: -750,
          y: 20
        }}
        particleColor="rainbow"
        particleSize={5}
      />
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
