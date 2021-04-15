import axios from 'axios'
import { 
    USER_LOGIN_REQUEST,
    USER_LOGIN_SUCCESS, 
    USER_LOGIN_FAIL,

    USER_LOGOUT,

    USER_REGISTER_REQUEST,
    USER_REGISTER_SUCCESS, 
    USER_REGISTER_FAIL, } from '../constants/userConstants'

// login functionality
export const login = (email, password) => async (dispatch) => {
    try {
        dispatch({
            type: USER_LOGIN_REQUEST
        })

        const config = {
            headers:{
                'Content-type':'application/json'
            }
        }
        // api call to user login
        const {data} = await axios.post(
            '/api/users/login/',
            {'username':email, 'password':password},
            config
            )

            dispatch({
                type:USER_LOGIN_SUCCESS,
                payload:data
            })

            localStorage.setItem('userInfo', JSON.stringify(data))

    } catch (error) {
        
        dispatch({
            type: USER_LOGIN_FAIL,
            payload: error.response && error.response.data.detail
            ? error.response.data.detail
            : error.message,
        })
    }

}

// logout functionality
export const logout = () => (dispatch) => {
    localStorage.removeItem('userInfo')
    dispatch({type:USER_LOGOUT})
}

// Register functionality

export const register = (name, email, password) => async (dispatch) => {
    try {
        dispatch({
            type: USER_REGISTER_REQUEST
        })

        const config = {
            headers:{
                'Content-type':'application/json'
            }
        }
        // api call to user login
        const {data} = await axios.post(
            '/api/users/register/',
            {'name': name, 'email':email, 'password':password},
            config
            )
            
            dispatch({
                type:USER_REGISTER_SUCCESS,
                payload:data
            })
            // After user register success, dispatch as login success
            dispatch({
                type:USER_LOGIN_SUCCESS,
                payload:data
            })

            localStorage.setItem('userInfo', JSON.stringify(data))

    } catch (error) {
        dispatch({
            type: USER_REGISTER_FAIL,
            payload: error.response && error.response.data.detail
            ? error.response.data.detail
            : error.message,
        })
    }

}
