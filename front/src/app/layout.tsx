import type { Metadata } from "next"
import { Inter } from "next/font/google"
import "./globals.css"
import Footer from "./components/footer"
import { Suspense } from "react";

const inter = Inter({ subsets: ["latin"] })

export const metadata: Metadata = {
  title: "xKaliburr",
  description: "Created by round table team",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode
}>) {
  return (
    <html lang="pt-BR">
      <body className={inter.className}>
        <main className="flex flex-col min-h-[calc(100vh_-_3.5rem)] p-8 bg-slate-800 items-center justify-center relative">
          <Suspense>
            {children}
          </Suspense>
        </main>
        <Footer />
      </body>
    </html>
  )
}
