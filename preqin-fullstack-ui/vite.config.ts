// import { defineConfig } from 'vite'
import { defineConfig } from 'vitest/config';
import react from '@vitejs/plugin-react-swc'
import path from 'path'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  resolve:{
    alias:{
      '@/': `${path.resolve(__dirname, 'src')}/`
    }
  },
  test: {
    // 👋 add the line below to add jsdom to vite
    environment: 'jsdom',
    // hey! 👋 over here
    globals: true,
    setupFiles: './src/setup.ts', // assuming the test folder is in the root of our project
  }
})
