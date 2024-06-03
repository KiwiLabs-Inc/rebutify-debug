import axios from 'axios'
// import {
//   updateUser
// } from '../Redux/reducers/user';

// INJECT STORE TO PREVENT IMPORT ISSUES
// let store
// export const injectStore = _store => {
//   store = _store
// }

// URLs
const baseURL = process.env.NEXT_PUBLIC_API_URL

// API INSTANCE
const api = axios.create({
  baseURL,
})

// # INTERCEPTORS #
// On request
api.interceptors.request.use(
  (req) => {
    // Add '/' at the end of URLs
    if (req.url && req.url[req.url.length - 1] !== '/') {
      req.url += '/'
    }

    // Add access token to header if it exists
    const access_token = localStorage.getItem('access_token')
    if (access_token !== 'null' && access_token !== 'undefined') {
      req.headers.access_token = localStorage.getItem('access_token')
    }

    console.log('# Intercepted request:', req)
    return req
  },
  function (err) {
    return Promise.reject(err)
  },
)

// On response
api.interceptors.response.use(
  (res) => {
    // Add tokens to local storage
    localStorage.setItem('access_token', res.data?.access)
    localStorage.setItem('refresh_token', res.data?.refresh)

    // Update user state if user is not logged in
    if (res.data.loggedIn === false) {
      // store.dispatch(
      //   updateUser(res.data)
      // )
    }

    console.log('# Intercepted response:', res)
    return res
  },
  function (err) {
    if (err?.response?.status === 429) {
      console.error('# Too many API requests: ', err.response.status)
    }
    if (err?.response?.status === 500) {
      console.error('# Internal server error: ', err.response.status)
    }
    return Promise.reject(err)
  },
)

export default api