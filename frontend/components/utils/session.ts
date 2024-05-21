// import { cookies } from "next/headers";
// import { headers } from "next/headers";
//
// export function getSessionID(): string | null {
//   const a = cookies().get("sessionid");
//   const b = headers().get("sessionid");
//   if (!a) {
//     return b;
//   } else {
//     return a.value;
//   }
// }
import { cookies } from "next/headers";
import { headers } from "next/headers";

export function getSessionID(): string | null {
  const a = cookies().get("sessionid");
  const b = headers().get("sessionid");

// `${existingCookies}; ${newCookie}`
  const existingCookies = cookies().toString();
  let sessionID = cookies().has("sessionid") ? cookies().get("sessionid")?.toString() : headers().get("sessionid")?.toString()
  headers: { Cookie: `${existingCookies}; ${sessionID}` }

  if (!cookies().has("sessionid")) {
    cookies().getAll()
    headers: { Cookie: cookies().toString() + sessionid },
    headers().get("sessionid");
    return b;
  } else {
    return a.value;
  }
}
