/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{html,js,svelte,ts}'],
  theme: {
    extend: {
      colors: {
        primaryColor: '#060606',
        secondaryColor: '#21212180', // 80 at the end represents 50% opacity
      },
      animation:{
        meteor:"meteor 5s linear infinite",
      },
      keyframes:{
        meteor:{
          "0%":{transform:"rotate(215deg) translateX(0)", opacity:1},
          "70%":{opacity:1},
          "100%":{
            transform:"rotate(215deg) translateX(-500px)",
            opacity:0,
          }
        }
      }
    },
  },
  plugins: [],
}

