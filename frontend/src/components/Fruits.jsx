import React, { useEffect, useState } from 'react';
import AddFruitForm from './AddFruitForm';
import api from '../api';

const FruitList = () => {
  const [fruits, setFruits] = useState([]);

  const fetchFruits = async () => {
    try {
      const response = await api.get('/fruits');
      setFruits(response.data.fruits);
    } catch (error) {
      console.error("Error fetching fruits", error);
    }
  };

  const addFruit = async (fruitName) => {
    try {
      await api.post('/fruits', { name: fruitName });
      fetchFruits();  // Refresh the list after adding a fruit
    } catch (error) {
      console.error("Error adding fruit", error);
    }
  };
  const removeFruit = async (fruitName) => {
    try {
      await api.delete('/fruits', { data: { name: fruitName } });
      fetchFruits();  // Refresh the list after removing a fruit
    } catch (error) {
      console.error("Error deleting fruit", error);
    }
  };

  useEffect(() => {
    fetchFruits();
  }, []);

  return (
    <div>
      <h2>Fruits List</h2>
      <ul>
        {fruits.map((fruit, index) => (
           <li key={index}>
          {fruit.name}{' '}
          <button
            type="button"
            onClick={() => removeFruit(fruit.name)}
          >
            Delete
          </button>
        </li>
        ))}
      </ul>
      <AddFruitForm addFruit={addFruit} />
    </div>
  );
};

export default FruitList;