import React from 'react';
import BedroomList from './components/BedroomList';
import './App.css';
import { MouseTrail } from 'retro-react';

const App = () => {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Nostalgic Bedrooms</h1>
      </header>
      <main>
        <BedroomList />
          <MouseTrail
            offset={{
              x: -750,
              y: 20
            }}
            particleColor="rainbow"
            particleSize={5}
          />
      </main>
    </div>
  );
};

export default App;
