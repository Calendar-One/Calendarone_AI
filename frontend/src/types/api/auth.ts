import type { User } from "./users"


export type TokenResponse = {
    access_token: string
    refresh_token: string
    token_type: string
    user: User
}


export type LogoutResponse = {
    message: string;
}