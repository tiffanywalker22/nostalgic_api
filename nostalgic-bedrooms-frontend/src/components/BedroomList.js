import React, { useEffect, useState } from 'react';
import { getBedrooms } from '../services/api';
import './BedroomList.css';

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
                        <div className="bedroom-card" key={bedroom.id}> {/* Card for each bedroom */}
                            <img
                                src={`http://localhost:5000/static/${bedroom.img_src}`}
                                lt={bedroom.title}
                                className="bedroom-img" // Optional: add class for image styling
                            />
                            <div className="bedroom-info">
                                <h5>{bedroom.title}</h5>
                                <p>{bedroom.description}</p>
                            </div>
                        </div>
                ))}
            </div>
        </div>
    );
};

export default BedroomList;