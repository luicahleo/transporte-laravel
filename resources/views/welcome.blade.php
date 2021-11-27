<!DOCTYPE html>
<html lang="{{ str_replace('_', '-', app()->getLocale()) }}">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="csrf-token" content="{{ csrf_token() }}">

    <title>Laravel</title>

    <!-- Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700&display=swap" rel="stylesheet">

    <!-- Styles -->
    <link href="{{ asset('css/app.css') }}" rel="stylesheet">

    <style>
        body {
            font-family: 'Nunito';
            background: #f7fafc;
        }
    </style>
</head>

<body>
    <div class="container-fluid fixed-top p-4">
        <div class="col-12">
            <div class="d-flex justify-content-end">
                @if (Route::has('login'))
                <div class="">
                    @auth
                    <a href="{{ url('/dashboard') }}" class="text-muted">Dashboard</a>
                    @else
                    <a href="{{ route('login') }}" class="text-muted">Log in</a>

                    @if (Route::has('register'))
                    <a href="{{ route('register') }}" class="ms-4 text-muted">Register</a>
                    @endif
                    @endif
                </div>
                @endif
            </div>
        </div>
    </div>

    <div class="container-fluid my-5 pt-5 px-5">
        <div class="row justify-content-center px-4">
            <div class="col-md-12 col-lg-9">
                <div class="card shadow-sm">
                    <div class="row">
                        <div class="col-md-6 pr-0">
                            <div class="card">

                                <div class="card-body border-right border-bottom p-3 h-100">
                                    <div class="text-primary">
                                        <h1>TRABAJO GRUPO 12</h1>

                                    </div>
                                    <div class="d-flex flex-row bd-highlight pt-2">
                                        <a href="{{ route('trabajo.index')}}">Hola Mundo PYTHON</a>
                                    </div>
                                </div>
                            </div>

                        </div>


                    </div>
                </div>


            </div>
        </div>
    </div>
</body>

</html>