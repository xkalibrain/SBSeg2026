import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./src/pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/components/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      backgroundImage: {
        "gradient-radial": "radial-gradient(var(--tw-gradient-stops))",
        "gradient-conic":
          "conic-gradient(from 180deg at 50% 50%, var(--tw-gradient-stops))",
      },
      colors: {
        "blue-kali": "rgba(37, 112, 223, 1)",
        "blue-gradient": "rgba(39, 127, 255, 1)",
        "purple-gradient": "rgba(150, 42, 195, 1)",
        "slate-kali": "rgba(53, 56, 67, 1)",
      }
    },
  },
  plugins: [],
};
export default config;
