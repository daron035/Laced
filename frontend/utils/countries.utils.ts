export type Size = {
  id: number;
  UK: number;
  EU: number;
  price: { GBP: number; EUR: number };
};

type Description = {
  ru: string;
  eu: string;
};

export type JsData = {
  sizes: Size[];
  description: Description;
};

const TWO_LETTER_KEY_LENGTH = 2;
const EXCLUDED_KEY = "id";

export function getCountries(data: Size[]): string[] {
  return Array.from(new Set(data.flatMap(getCountryKeys)));
}

function getCountryKeys(size: Size): string[] {
  return Object.keys(size).filter(isValidCountryKey);
}

function isValidCountryKey(key: string): boolean {
  return key.length === TWO_LETTER_KEY_LENGTH && key !== EXCLUDED_KEY;
}

const jsData = {
  sizes: [
    ['id', 'UK', 'EU',  ["GBP", "EUR"]],
    [
      [33, 3.3, 36, [130, 160]],
      [41, 4.0, 37, [140, 180]]
    ]
  ]
}
// console.log(jsData)

const countryCodes = jsData.sizes[0].slice(1, -1);

console.log('000000', countryCodes);
