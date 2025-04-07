/** @type {import('tailwindcss').Config} */
export default {
    content: [
      "./index.html",
      "./src/**/*.{js,ts,jsx,tsx}",
    ],
    safelist: [
      // Yellow
      'bg-yellow-300',
      'border-yellow-500',
      
      // Red
      'bg-red-200',
      'border-red-400',
  
      // Black (gray)
      'bg-gray-800',
      'text-white',
      'border-gray-600',
    ],
    theme: {
      extend: {},
    },
    plugins: [],
  }
  