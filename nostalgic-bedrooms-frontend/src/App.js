import React from 'react';
import BedroomList from './components/BedroomList';
import './App.css';
import { Box, Container, MouseTrail, Text, Scrollbar } from 'retro-react';

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
            // backgroundColor: 'w',
            height: '100vh',
            overflowY: 'scroll',
            padding: '1rem',
            width: '100vw',
            boxSizing: 'border-box',
            // boxSizing: 'border-box' // includes padding in height calculation
          }}
        >
          <header className="App-header">
            <Box
              color="primary"
              pattern="solid"
              sx={{
                width: '100%'
              }}
            >
              <Text
                align="center"
                color="rainbow"
                variant="h2"
              >
                <h2>Nostalgic Bedrooms</h2>
              </Text>
            </Box>
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
