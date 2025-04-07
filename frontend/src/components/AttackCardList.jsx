import { useEffect, useState } from 'react';
import api from '../api/axios';

export default function AttackCardList() {
  const [cards, setCards] = useState([]);

  useEffect(() => {
    api.get('attack_cards/')
      .then(response => setCards(response.data))
      .catch(error => console.error('Error fetching attack cards:', error));
  }, []);

  const getCardColor = (type) => {
    const normalized = type?.toUpperCase();
    console.log('getCardColor called with:', type, '→ normalized:', normalized);

    switch (normalized) {
        case 'YELLOW':
            return 'bg-yellow-300 border-yellow-500 text-black';          
      case 'RED':
        return 'bg-red-200 border-red-400';
      case 'BLACK':
        return 'bg-gray-800 text-white border-gray-600';
      default:
        return 'bg-white border-gray-300';
    }
  };

  return (
    <div className="p-4">
      <h2 className="text-2xl font-bold mb-4 text-center">Attack Cards</h2>
      <div className="grid gap-4 grid-cols-1 md:grid-cols-2 lg:grid-cols-3">
        {cards.map(card => {
          console.log(card.card_type); // Debug line to inspect card types

          return (
                <div
                key={card.id}
                className={`border-2 rounded-lg shadow p-4 transition hover:scale-[1.02] ${getCardColor(card.card_type)} text-black min-h-[100px]`}
                >

              <div className="flex justify-between items-center mb-2">
                <h3 className="text-lg font-semibold">{card.name}</h3>
                <span className="text-xs px-2 py-1 rounded-full bg-white/30 border">
                  {card.card_type}
                </span>
              </div>
              <p className="text-sm">{card.description}</p>
            </div>
          );
        })}
      </div>
      <div className="bg-yellow-300 border-yellow-500 text-black border-2 p-4 mt-8 rounded">
  This box should be yellow.
</div>

    </div>
  );
}