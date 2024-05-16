import continueWithSocialAuth from "./continue-with-social-auth";

export const continueWithGoogle = () =>
  continueWithSocialAuth("google-oauth2", "google");
export const continueWithVk = () => continueWithSocialAuth("vk-oauth2", "vk");

export { getCookie, getResponseCookie, getAllCookies, setCookie, deleteCookie } from "./cookie";
