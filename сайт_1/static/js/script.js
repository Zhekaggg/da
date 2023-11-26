document.addEventListener("DOMContentLoaded", function () {
  const genreButtons = document.querySelectorAll("#genre-buttons button");
  const movieCards = document.querySelectorAll(".movie-card");

  function filterMoviesByGenre(genreId) {
    movieCards.forEach((card) => {
      const cardGenres = card.getAttribute("data-genre").split(",");
      if (cardGenres.includes(genreId)) {
        card.style.display = "block";
      } else {
        card.style.display = "none";
      }
    });
  }

  genreButtons.forEach((button) => {
    button.addEventListener("click", function () {
      const genreId = button.getAttribute("data-genre");
      filterMoviesByGenre(genreId);
    });
  });

  // Добавляем обработчик для кнопки "Подробнее"
  movieCards.forEach((card) => {
    const detailsButton = card.querySelector(".btn-details");
    const modal = card.querySelector(".modal");
    const closeBtn = card.querySelector(".close");
    const description = card.querySelector(".description");

    detailsButton.addEventListener("click", function () {
      modal.style.display = "block";
      description.style.display = "block";
    });

    closeBtn.addEventListener("click", function () {
      modal.style.display = "none";
      description.style.display = "none";
    });
  });
});
