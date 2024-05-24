import React from 'react';

const Tiles = () => {
  const tiles = Array.from({ length: 32 }, (_, i) => i + 1);

  const handleClick = (tileNumber) => {
    // Replace with your actual endpoint and port
    const endpoint = `http://localhost:8000/api/tile/${tileNumber}`;

    // Call the endpoint
    fetch(endpoint)
      .then(response => response.json())
      .then(data => console.log(data))
      .catch(error => console.error('Error:', error));
  };

  return (
    <table>
      <tbody>
        {tiles.map((tile, index) => {
          return index % 4 === 0 ? (
            <tr key={index}>
              {tiles.slice(index, index + 4).map((tile) => (
                <td key={tile}>
                  <button onClick={() => handleClick(tile)}>{`Tile ${tile}`}</button>
                </td>
              ))}
            </tr>
          ) : null;
        })}
      </tbody>
    </table>
  );
};

export default Tiles;