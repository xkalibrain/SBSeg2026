const BASE_URL = process.env.NEXT_PUBLIC_API_ADDRESS ?? "/api"

export function customFetch(endpoint: string, options: RequestInit) {
  return fetch(`${BASE_URL}${endpoint}`, options)
}
