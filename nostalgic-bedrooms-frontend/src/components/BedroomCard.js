import React from 'react';

const BedroomCard = ({ bedroom }) => {
  return (
    <div className="bedroom-card">
      <h2>{bedroom.name}</h2>
      <img src={bedroom.image_url} alt={bedroom.name} />
      <p>{bedroom.description}</p>
    </div>
  );
};

export default BedroomCard;