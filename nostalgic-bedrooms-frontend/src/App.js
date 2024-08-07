import React from 'react';
import BedroomList from './components/BedroomList';
import './App.css';
import { MouseTrail } from 'retro-react';
import { Scrollbar } from 'retro-react';

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
      <Scrollbar theme="primary">
        <div
          style={{
            backgroundColor: 'white',
            height: '100%',
            overflowY: 'scroll',
            padding: '1rem',
            boxSizing: 'border-box' // includes padding in height calculation
          }}
        >
          <header className="App-header">
            <h1>Nostalgic Bedrooms</h1>
          </header>
          <main>
            <BedroomList />
          </main>
        </div>
    </Scrollbar>
  </div>
  );
};

export default App;
