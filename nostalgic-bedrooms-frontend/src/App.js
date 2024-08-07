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
        <Container
          sx={{
            border: '1px solid black',
            height: '500px',
            position: 'relative',
            width: '500px'
          }}
        >
          <MouseTrail
            offset={{
              x: 0,
              y: 0
            }}
            particleColor="rainbow"
            particleSize={5}
          />
        </Container>
      </main>
    </div>
  );
};

export default App;
