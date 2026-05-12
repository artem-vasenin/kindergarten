import axios from 'axios';
import { useProfileStore } from "@/store/profile.store.ts";

export const http = axios.create({
    baseURL: 'http://localhost:8000/api/admin',
    timeout: 10000,
    headers: {
        'Content-Type': 'application/json',
    },
});

http.interceptors.request.use((config) => {
  const store = useProfileStore();

  if (store.token) {
        config.headers.Authorization = `Bearer ${store.token}`;
    }
    return config;
});
