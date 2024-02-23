"use client"

import React, { useEffect, useState } from 'react';

function page() {

  const [message, setMessage] = useState("Loading")
  const [pokemon, setPokemon] = useState([])

  useEffect(() => {
    fetch("http://localhost:8080/api/pokedex")
      .then((response) => response.json())
      .then((data) => {
        setMessage(data.message);
        setPokemon(data.pokemon);
        console.log(pokemon)
      });
  }, []);

  return (
    <div>
      <div>{message}</div>

      {pokemon.map((pokemon, index) => (
        <div key={index}>
          {pokemon}
        </div>
      ))}

    </div>
  )
}

export default page

