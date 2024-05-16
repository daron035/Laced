export function getCookie(name: string): string | undefined {
  let matches = document.cookie.match(
    new RegExp(
      "(?:^|; )" + name.replace(/([.$?*|{}()[\]\\/+^])/g, "\\$1") + "=([^;]*)",
    ),
  );
  return matches ? decodeURIComponent(matches[1]) : undefined;
}

export function getResponseCookie(name: string, response: any): string | undefined {
  const cookieHeader = response.headers.get("Set-Cookie");
  if (!cookieHeader) {
    return undefined; // Если заголовок Set-Cookie отсутствует, возвращаем undefined
  }
  
  const matches = cookieHeader.match(
    new RegExp(
      "(?:^|; )" + name.replace(/([.$?*|{}()[\]\\/+^])/g, "\\$1") + "=([^;]*)",
    ),
  );
  return matches ? decodeURIComponent(matches[1]) : undefined;
}


// export function getAllCookies(): { [key: string]: string } | undefined {
export function getAllCookies(): { [key: string]: string } {
  // if (!document.cookie) {
  //   return undefined; // Возвращаем undefined, если нет cookies
  // }

  const cookies: { [key: string]: string } = {};

  document.cookie.split(";").forEach((cookie) => {
    const parts = cookie.split("=");
    const name = parts[0].trim();
    const value = decodeURIComponent(parts[1]);
    cookies[name] = value;
  });

  return cookies;
}

export function setCookie(
  name: string,
  value: string,
  options: Record<string, any> = {},
): void {
  options = {
    path: "/",
    // при необходимости добавьте другие значения по умолчанию
    ...options,
  };

  if (options.expires instanceof Date) {
    options.expires = options.expires.toUTCString();
  }

  let updatedCookie =
    encodeURIComponent(name) + "=" + encodeURIComponent(value);

  for (let optionKey in options) {
    updatedCookie += "; " + optionKey;
    let optionValue = options[optionKey];
    if (optionValue !== true) {
      updatedCookie += "=" + optionValue;
    }
  }

  document.cookie = updatedCookie;
}

export function deleteCookie(name: string): void {
  setCookie(name, "", {
    "max-age": -1,
  });
}
