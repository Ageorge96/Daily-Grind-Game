import { render, screen } from "@testing-library/react";
import { BrowserRouter } from "react-router-dom";

describe("Quiz game", () => {
    Test("renders title", () => {

        render(
            <BrowserRouter>
              <QuizPage />
            </BrowserRouter>
          );

        const heading  = screen.getByRole("heading");
        expect(heading.textContent).toEqual("Quiz Game")
    })
})