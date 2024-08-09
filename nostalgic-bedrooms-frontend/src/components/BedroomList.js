import React, { useEffect, useState } from 'react';
import { getBedrooms } from '../services/api';
import './BedroomList.css';
import { Box, Card, Text, Divider } from 'retro-react';
// const BedroomList = () => {
//     const [bedrooms, setBedrooms] = useState([]);

//     useEffect(() => {
//         getBedrooms()
//             .then(data => setBedrooms(data))
//             .catch(error => console.error(error));
//     }, []);

//     return (
//         <div className="bedroom-list-container">
//             <div className="row">
//                 {bedrooms.map(bedroom => (
//                     <div className="bedroom-card" key={bedroom.id}> {/* Card for each bedroom */}
//                         <img
//                             src={`http://localhost:5000/static/${bedroom.img_src}`}
//                             lt={bedroom.title}
//                             className="bedroom-img" // Optional: add class for image styling
//                         />
//                         <div className="bedroom-info">
//                             <h5>{bedroom.title}</h5>
//                             <Divider
//                                 color="rainbow"
//                                 orientation="horizontal"
//                             />
//                             <p>{bedroom.description}</p>
//                         </div>
//                     </div>
//                 ))}
//             </div>
//         </div>
//     );
// };

// export default BedroomList;

const BedroomList = () => {
  const [bedrooms, setBedrooms] = useState([]);

  useEffect(() => {
      getBedrooms()
          .then(data => setBedrooms(data))
          .catch(error => console.error(error));
  }, []);

  return (
      <div className="bedroom-list-container">
          <div className="row">
              {bedrooms.map(bedroom => (
                  <Box
                      key={bedroom.id}
                      sx={{
                          alignItems: 'center',
                          display: 'flex',
                          justifyContent: 'center',
                          marginBottom: '20px', // Optional: add margin between cards
                      }}
                  >
                      <Card
                          alt={bedroom.title}
                          color="primary"
                          // footer={<Text variant="small">#{bedroom.id}</Text>} // Optional footer, like an ID
                          header={
                          <div>
                            <Text align="center" variant="h5">{bedroom.title}</Text>
                            <Divider
                                color="rainbow"
                                orientation="horizontal"
                            />
                          </div>
                          }
                          image={`http://localhost:5000/static/${bedroom.img_src}`}
                          pattern="noise"
                          sx={{
                              maxHeight: '800px',
                              maxWidth: '500px',
                              width: '100%',  // Ensures the card fits within the container
                          }}
                      >
                          <Text variant="paragraph">
                              {bedroom.description}
                          </Text>
                      </Card>
                  </Box>
              ))}
          </div>
      </div>
  );
};

export default BedroomList;