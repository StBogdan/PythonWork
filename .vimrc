set nocompatible              " be iMproved, required
filetype off                  " required

" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
" alternatively, pass a path where Vundle should install plugins
"call vundle#begin('~/some/path/here')

" let Vundle manage Vundle, required
Plugin 'VundleVim/Vundle.vim'

" Keep Plugin commands between vundle#begin/end.
" plugin on GitHub repo
Plugin 'tpope/vim-fugitive'

" The sparkup vim script is in a subdirectory of this repo called vim.
" Pass the path to set the runtimepath properly.
Plugin 'rstacruz/sparkup', {'rtp': 'vim/'}

" Check sintax on save
Plugin 'vim-syntastic/syntastic'

" Filesystem nav
Plugin 'preservim/nerdtree'

" Autocompletion (YCM)
Bundle 'Valloric/YouCompleteMe'

" Nice bottom line
Plugin 'vim-airline/vim-airline'

" All of your Plugins must be added before the following line
call vundle#end()            " required
filetype plugin indent on    " required

syntax on  "duh
colorscheme molokai "https://github.com/tomasr/molokai
set clipboard=unnamed "System clipboard
set encoding=utf-8 "Support for Python3 files
set mouse=a "mouse input
set backspace=2
set nu "line numbering
set background=dark 
set cursorline "indicate line
set showmatch "match brachkets

"See https://realpython.com/vim-and-python-a-match-made-in-heaven/
"Screen split navigation
"https://linuxhint.com/how-to-use-vim-split-screen/s
nnoremap <C-J> <C-W><C-J>
nnoremap <C-K> <C-W><C-K>
nnoremap <C-L> <C-W><C-L>
nnoremap <C-H> <C-W><C-H>


" Enable folding
set foldmethod=indent
set foldlevel=99

" PEP 8 Indents
au BufNewFile, BufRead *.py
    \ set tabstop=4
    \   set softtabstop=4
    \   set shiftwidth=4
    \   set textwidth=79
    \   set expandtab
    \   set autoindent
    \   set fileformat=unix

" Key maps
map <C-e> :NERDTreeToggle<CR>
