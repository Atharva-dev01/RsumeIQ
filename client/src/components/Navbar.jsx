import { Link } from "react-router-dom";
import { Menu } from "lucide-react";

function Navbar() {
  return (
    <nav className="sticky top-0 z-50 bg-slate-950/80 backdrop-blur-md border-b border-slate-800">
      <div className="max-w-7xl mx-auto px-6 py-4 flex items-center justify-between">

        {/* Logo */}
        <Link
          to="/"
          className="text-3xl font-bold tracking-wide"
        >
          <span className="text-white">Resume</span>
          <span className="text-cyan-400">IQ</span>
        </Link>

        {/* Desktop Navigation */}
        <div className="hidden md:flex items-center gap-8">

          <Link
            to="/"
            className="text-slate-300 hover:text-cyan-400 transition-colors duration-300"
          >
            Home
          </Link>

          <Link
            to="/dashboard"
            className="text-slate-300 hover:text-cyan-400 transition-colors duration-300"
          >
            Dashboard
          </Link>

          <Link
            to="/login"
            className="text-slate-300 hover:text-cyan-400 transition-colors duration-300"
          >
            Login
          </Link>

          <Link
            to="/register"
            className="bg-gradient-to-r from-blue-600 to-cyan-500 text-white px-5 py-2 rounded-lg font-medium hover:scale-105 transition duration-300 shadow-lg"
          >
            Register
          </Link>

        </div>

        {/* Mobile Menu Icon */}
        <button className="md:hidden text-white">
          <Menu size={28} />
        </button>

      </div>
    </nav>
  );
}

export default Navbar;