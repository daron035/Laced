// import requestIp from "request-ip";
// import { NextResponse } from "next/server";
//
// // export async function GET(request: Request) {
// export async function GET() {
//   console.log("23");
//   return NextResponse.json({ message: "Hello" });
// }
//
// // const detectedIp = requestIp.getClientIp(req)

// import { NextRequest, NextResponse } from "next/server";
// // import requestIp from "request-ip";
//
// // export default function handler(req: NextRequest, res: NextResponse) {
// export async function GET(req: NextRequest, res: NextResponse) {
//   const requestIp = require("request-ip");
//   const detectedIp = await requestIp.getClientIp(req);
//   console.log(detectedIp);
//   // const clientIP =
//   //   req.headers["x-forwarded-for"] || req.connection.remoteAddress;
//   // res.status(200).json({ clientIP });
//   // res.status(200).json({ detectedIp });
//   return NextResponse.json({ message: detectedIp });
// }

// import { NextRequest, NextResponse } from "next/server";
// // import requestIp from "request-ip";
//
// export function handler(req: NextRequest, res: NextResponse) {
//   const requestIp = require("request-ip");
//   const clientIp = requestIp.getClientIp(req);
//   // res.status(200).json({ clientIp });
//   return NextResponse.json({ message: clientIp });
// }

// import { NextRequest, NextResponse } from "next/server";
//
// type Data = {
//   ip: string;
// };
//
// export async function GET(req: NextRequest) {
//   let ip = req.headers["x-real-ip"] as string;
//
//   const forwardedFor = req.headers["x-forwarded-for"] as string;
//   if (!ip && forwardedFor) {
//     ip = forwardedFor?.split(",").at(0) ?? "Unknown";
//   }
//
//   // res.status(200).json({ ip: ip });
//   // res.status(200).json({ ip: "asdfs" });
//   console.log(ip);
//   return NextResponse.json({ message: ip });
// }

import { NextRequest, NextResponse } from "next/server";
// export async function GET(req: NextRequest) {
export default function GET(req: NextRequest, res: NextResponse) {
  let ip;

  if (req.headers["x-forwarded-for"]) {
    ip = req.headers["x-forwarded-for"].split(",")[0];
  } else if (req.headers["x-real-ip"]) {
    ip = req.connection.remoteAddress;
  } else {
    ip = req.connection.remoteAddress;
  }

  console.log(ip);

  console.log(ip);
  res.status(200).json({ name: "John Doe" });
}
