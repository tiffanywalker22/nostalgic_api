import axios from 'axios';

const API_URL = 'http://localhost:5000';

export const getBedrooms = async () => {
  try {
    const response = await axios.get(`${API_URL}/bedrooms`);
    return response.data;
  } catch (error) {
    console.error('Error fetching bedrooms:', error);
    throw error;
  }
};