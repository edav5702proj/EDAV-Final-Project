# Quick render: only work for same-level .rmd file
# fname can be any .Rmd file
quick_build <- function(fname){
  name = sprintf("%s.Rmd", fname)
  bookdown::render_book(name)
  browseURL(sprintf("docs/%s.html", fname))
}
# Run this to render
quick_build("index")


