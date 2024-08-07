import React, { useEffect, useState } from 'react';
import { getBedrooms } from '../services/api';
import BedroomCard from './BedroomCard';

const BedroomList = () => {
  const [bedrooms, setBedrooms] = useState([]);

  useEffect(() => {
    const fetchBedrooms = async () => {
      try {
        const data = await getBedrooms();
        setBedrooms(data);
      } catch (error) {
        console.error('Error fetching bedrooms:', error);
      }
    };

    fetchBedrooms();
  }, []);

  return (
    <div className="bedroom-list">
      {bedrooms.map(bedroom => (
        <BedroomCard key={bedroom.id} bedroom={bedroom} />
      ))}
    </div>
  );
};

export default BedroomList;