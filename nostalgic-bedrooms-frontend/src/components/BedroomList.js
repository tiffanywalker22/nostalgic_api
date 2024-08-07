import React, { useEffect, useState } from 'react';
import { getBedrooms } from '../services/api';

const BedroomList = () => {
    const [bedrooms, setBedrooms] = useState([]);

    useEffect(() => {
        getBedrooms()
            .then(data => setBedrooms(data))
            .catch(error => console.error(error));
    }, []);

    return (
        <div className="container">
            <div className="row">
                {bedrooms.map(bedroom => (
                    <div className="col-md-4" key={bedroom.id}>
                        <div className="card">
                            <img src={`http://localhost:5000/${bedroom.image_url}`} className="card-img-top" alt={bedroom.name} />
                            <div className="card-body">
                                <h5 className="card-title">{bedroom.name}</h5>
                                <p className="card-text">{bedroom.description}</p>
                            </div>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default BedroomList;