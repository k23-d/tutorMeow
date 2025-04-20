import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import path from 'path'
import FileUpload from '@/components/UploadSection.vue'


export default defineConfig({
  plugins: [vue()],
  server: {
    port: 3000
  },
  resolve: {
    alias: {
      '@': path.resolve(__dirname, 'src')
    }
  }
})
