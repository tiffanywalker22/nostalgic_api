import React from 'react';
import BedroomList from './components/BedroomList';
import './App.css';
import { Container, MouseTrail } from 'retro-react';
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
          fluid
          sx={{
            backgroundColor: 'white',
            height: '100vh',
            overflowY: 'scroll',
            padding: '1rem',
            width: '100vw',
            boxSizing: 'border-box',
            // boxSizing: 'border-box' // includes padding in height calculation
          }}
        >
          <header className="App-header">
            <h1>Nostalgic Bedrooms</h1>
          </header>
          <main>
            <BedroomList />
          </main>
        </Container>
    </Scrollbar>
  </div>
  );
};

export default App;
