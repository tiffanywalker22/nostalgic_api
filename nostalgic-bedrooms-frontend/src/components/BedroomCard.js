import React from 'react';

const BedroomCard = ({ bedroom }) => {
  return (
    <div className="bedroom-card">
      <h2>{bedroom.title}</h2>
      <img src={bedroom.img_src} alt={bedroom.title} />
      <p>{bedroom.description}</p>
    </div>
  );
};

export default BedroomCard;