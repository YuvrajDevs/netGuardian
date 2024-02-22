"use client"
import Link from 'next/link';

const Nav = ({ isLoggedIn, onSignOut }) => {
  return (
    <nav>
      <div className="logo font-oswald-title mx-5 mt-4">
        <span className="text-[#4F96FB]">Net</span>
        <span className="text-black">Guardian</span>
      </div>
      {isLoggedIn ? (
        <button onClick={onSignOut}>Sign Out</button>
      ) : null}
    </nav>
  );
};

export default Nav;
