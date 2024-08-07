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
  <Container
    sx={{
      backgroundColor: 'white',
      height: '300px',
      overflowY: 'scroll',
      padding: '1rem',
      width: '300px'
    }}
  >
  </Container>
</Scrollbar>
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
