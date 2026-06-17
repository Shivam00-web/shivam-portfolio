export default function Footer() {
  const year = new Date().getFullYear();

  return (
    <footer className="footer">
      <div className="container">
        <p>Copyright &copy; {year} by Shivam | All Rights Reserved</p>
      </div>
    </footer>
  );
}
