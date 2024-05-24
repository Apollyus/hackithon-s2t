import React from 'react';

const Tiles = () => {
  const tiles = Array.from({ length: 32 }, (_, i) => i + 1);

  return (
    <table>
      <tbody>
        {tiles.map((tile, index) => {
          return index % 4 === 0 ? (
            <tr key={index}>
              {tiles.slice(index, index + 4).map((tile) => (
                <td key={tile}>
                  <button>{`Tile ${tile}`}</button>
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