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
          <header>
            <h1 class="rainbow-letters">
              <span>N</span>
              <span>o</span>
              <span>s</span>
              <span>t</span>
              <span>a</span>
              <span>l</span>
              <span>g</span>
              <span>i</span>
              <span>a</span>
            </h1>
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
