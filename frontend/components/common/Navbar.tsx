"use client";

import Image from "next/image";
import Link from "next/link";
import { useEffect } from "react";
import Loading from "./Loading";

import { useLogoutMutation } from "@/redux/features/authApiSlice";
import { logout as setLogout } from "@/redux/features/authSlice";
import { getCart } from "@/redux/features/cartSlice";
import { useAppDispatch, useAppSelector } from "@/redux/hooks";

import "@/styles/navBar.sass";
import { Bag, Burger, Search } from "./svgs";
import fallback from "@/public/logo.svg";

export default function Navbar() {
  const dispatch = useAppDispatch();

  useEffect(() => {
    dispatch(getCart());
  }, [dispatch]);

  const [logout] = useLogoutMutation();

  const { isAuthenticated, isLoading } = useAppSelector((state) => state.auth);
  const { count } = useAppSelector((state) => state.cart);

  const handleLogout = () => {
    logout(undefined)
      .unwrap()
      .then(() => {
        dispatch(setLogout());
      });
  };

  const authLinks = (
    <>
      <Link href="#">
        <button className="btn">My Laced</button>
      </Link>
      <div className="dropdown_content">
        <Link href="#">Selling</Link>
        <Link href="#">Your Orders</Link>
        <Link href="#">Your Account</Link>
        <Link href="/users/sign_in" onClick={handleLogout}>
          Logout
        </Link>
      </div>
    </>
  );

  const guestLinks = (
    <Link href="/users/sign_in">
      <button className="btn">Log In</button>
    </Link>
  );

  return (
    <header className="hdr">
      <div className="hdr__inner">
        <div className="hdr__burger">
          <Burger width="25px" height="25px" fill="#101010" />
        </div>
        <div className="hdr__logo">
          <Link href="/">
            <Image
              // src="/logo.svg"
              src={fallback}
              width={72}
              height={72}
              alt=""
              className="min-w-[72px] max-h-[72px]"
            />
          </Link>
        </div>
        <nav className="nav">
          <ul className="nav__list">
            <li className="nav__item">
              <button className="btn">New Releases</button>
              <div className="dropdown_content">
                <a href="#">Link 1</a>
                <a href="#">Link 2</a>
                <a href="#">Link 3</a>
                <a href="#">Link 4</a>
              </div>
            </li>
            <li className="nav__item">
              <button className="btn">Best Sellers</button>
              <div className="dropdown_content">
                <a href="#">Link 1</a>
                <a href="#">Link 2</a>
                <a href="#">Link 3</a>
                <a href="#">Link 4</a>
              </div>
            </li>
            <li className="nav__item">
              <button className="btn">Browse</button>
            </li>
            <li className="nav__item">
              <button className="btn">Sell</button>
            </li>
            <li className="nav__item">
              {isLoading ? (
                <Loading />
              ) : isAuthenticated ? (
                authLinks
              ) : (
                guestLinks
              )}
            </li>
          </ul>
        </nav>
        <div className="hdr__actions flex gap-2 items-center select-none">
          <div className="cursor-pointer py-6 px-4">
            <Search width="25px" height="25px" fill="#101010" />
          </div>
          <div className="cursor-pointer py-6 px-4 relative">
            <Bag width="25px" height="25px" fill="#101010" />
            {count !== 0 && (
              <div className="bg-black flex justify-center items-center w-[18px] h-[18px] text-xs text-white rounded-full absolute top-5 left-[30px]">
                {count}
              </div>
            )}
          </div>
        </div>
      </div>
    </header>
  );
}
